// =========================================================
// CareerGraph Frontend
// =========================================================
//
// Responsibilities:
// 1. Load the user's skills.
// 2. Find career matches.
// 3. Display career cards.
// 4. Load career details.
// 5. Display missing skills.
// 6. Display recommended courses.
// 7. Display companies.
// 8. Display recommended projects.
// 9. Handle loading, empty, and error states.
// =========================================================


// =========================================================
// 1. Application Configuration
// =========================================================

// Demo user used by our seeded database.
const USER_ID = "user_001";


// =========================================================
// 2. API Helper
// =========================================================

/**
 * Send a request to our Flask API and return the data.
 *
 * @param {string} url - API endpoint.
 * @returns {Promise<Array|Object>} API response data.
 */
async function fetchAPI(url) {

    try {

        const response = await fetch(url);


        // -------------------------------------------------
        // Check HTTP status
        // -------------------------------------------------

        if (!response.ok) {

            let message =
                `Request failed (${response.status})`;


            // Try to get the backend error message
            try {

                const errorData =
                    await response.json();


                if (errorData.message) {

                    message =
                        errorData.message;
                }

            } catch {

                // Ignore JSON parsing errors.
            }


            throw new Error(message);
        }


        // -------------------------------------------------
        // Convert response to JSON
        // -------------------------------------------------

        const result =
            await response.json();


        // -------------------------------------------------
        // Check application-level success
        // -------------------------------------------------

        if (!result.success) {

            throw new Error(
                result.message ||
                "Something went wrong."
            );
        }


        return result.data;

    }

    catch (error) {

        console.error(
            "API Error:",
            error
        );

        throw error;
    }
}


// =========================================================
// 3. DOM Helper Functions
// =========================================================

/**
 * Show an HTML element.
 *
 * @param {string} id - Element ID.
 */
function showElement(id) {

    const element =
        document.getElementById(id);


    if (element) {

        element.classList.remove("hidden");
    }
}


/**
 * Hide an HTML element.
 *
 * @param {string} id - Element ID.
 */
function hideElement(id) {

    const element =
        document.getElementById(id);


    if (element) {

        element.classList.add("hidden");
    }
}


/**
 * Set the HTML content of an element.
 *
 * @param {string} id - Element ID.
 * @param {string} html - HTML content.
 */
function setHTML(id, html) {

    const element =
        document.getElementById(id);


    if (element) {

        element.innerHTML = html;
    }
}


// =========================================================
// 4. Load User Skills
// =========================================================

async function loadUserSkills() {

    // -----------------------------------------------------
    // Initial UI state
    // -----------------------------------------------------

    showElement("skills-loading");

    hideElement("skills-error");

    hideElement("skills-empty");

    hideElement("skills-container");


    try {

        // -------------------------------------------------
        // Request skills from Flask API
        // -------------------------------------------------

        const skills =
            await fetchAPI(
                `/api/users/${USER_ID}/skills`
            );


        // -------------------------------------------------
        // Hide loading state
        // -------------------------------------------------

        hideElement("skills-loading");


        const container =
            document.getElementById(
                "skills-container"
            );


        if (!container) {

            return;
        }


        // Remove previous skills
        container.innerHTML = "";


        // -------------------------------------------------
        // Empty state
        // -------------------------------------------------

        if (!skills || skills.length === 0) {

            showElement("skills-empty");

            return;
        }


        // -------------------------------------------------
        // Display skills
        // -------------------------------------------------

        for (const skill of skills) {

            const chip =
                document.createElement("div");


            chip.className =
                "skill-chip";


            chip.textContent =
                `${skill.name} · ${skill.proficiency}`;


            container.appendChild(chip);
        }


        // Show skill list
        showElement("skills-container");

    }

    catch (error) {

        console.error(
            "Unable to load user skills:",
            error
        );


        hideElement("skills-loading");

        hideElement("skills-container");

        showElement("skills-error");
    }
}


// =========================================================
// 5. Load Career Matches
// =========================================================

async function loadCareerMatches() {

    const button =
        document.getElementById(
            "find-careers-btn"
        );


    // -----------------------------------------------------
    // Disable button while request is running
    // -----------------------------------------------------

    if (button) {

        button.disabled = true;

        button.textContent =
            "Finding Careers...";
    }


    // -----------------------------------------------------
    // Initial UI state
    // -----------------------------------------------------

    showElement("careers-loading");

    hideElement("careers-empty");

    hideElement("careers-error");


    const container =
        document.getElementById(
            "careers-container"
        );


    if (container) {

        container.innerHTML = "";
    }


    try {

        // -------------------------------------------------
        // Request career matches
        // -------------------------------------------------

        const careers =
            await fetchAPI(
                `/api/users/${USER_ID}/career-matches`
            );


        hideElement("careers-loading");


        // -------------------------------------------------
        // Empty state
        // -------------------------------------------------

        if (!careers || careers.length === 0) {

            showElement("careers-empty");

            return;
        }


        // -------------------------------------------------
        // Display career cards
        // -------------------------------------------------

        for (const career of careers) {

            const card =
                createCareerCard(career);


            container.appendChild(card);
        }


        // -------------------------------------------------
        // Scroll to careers
        // -------------------------------------------------

        const careersSection =
            document.getElementById(
                "careers"
            );


        if (careersSection) {

            careersSection.scrollIntoView({
                behavior: "smooth"
            });
        }

    }

    catch (error) {

        console.error(
            "Unable to load career matches:",
            error
        );


        hideElement("careers-loading");

        showElement("careers-error");
    }

    finally {

        // -------------------------------------------------
        // Re-enable button
        // -------------------------------------------------

        if (button) {

            button.disabled = false;

            button.textContent =
                "Find My Career Matches";
        }
    }
}


// =========================================================
// 6. Create Career Card
// =========================================================

function createCareerCard(career) {

    const card =
        document.createElement("article");


    card.className =
        "career-card";


    // -----------------------------------------------------
    // Calculate safe percentage
    // -----------------------------------------------------

    let percentage =
        Number(
            career.match_percentage || 0
        );


    // Keep percentage between 0 and 100
    percentage =
        Math.max(
            0,
            Math.min(
                100,
                percentage
            )
        );


    // -----------------------------------------------------
    // Create card HTML
    // -----------------------------------------------------

    card.innerHTML = `

        <h3>
            ${escapeHTML(career.title)}
        </h3>


        <p class="career-description">
            ${escapeHTML(career.description)}
        </p>


        <div class="match-row">

            <span class="match-label">
                Skill match
            </span>


            <span class="match-value">
                ${percentage}%
            </span>

        </div>


        <div class="progress">

            <div
                class="progress-bar"
                style="width: ${percentage}%"
            ></div>

        </div>


        <p class="muted">

            ${Number(career.matching_skills || 0)}

            of

            ${Number(career.total_required_skills || 0)}

            required skills

        </p>

    `;


    // -----------------------------------------------------
    // Click career card
    // -----------------------------------------------------

    card.addEventListener(
        "click",
        () => {

            loadCareerDetails(career);
        }
    );


    return card;
}


// =========================================================
// 7. Load Career Details
// =========================================================

async function loadCareerDetails(career) {

    const section =
        document.getElementById(
            "career-details"
        );


    if (!section) {

        return;
    }


    // -----------------------------------------------------
    // Show career details section
    // -----------------------------------------------------

    section.classList.remove("hidden");


    // -----------------------------------------------------
    // Display selected career name
    // -----------------------------------------------------

    const title =
        document.getElementById(
            "selected-career-title"
        );


    if (title) {

        title.textContent =
            career.title;
    }


    // -----------------------------------------------------
    // Scroll to details
    // -----------------------------------------------------

    section.scrollIntoView({
        behavior: "smooth"
    });


    // -----------------------------------------------------
    // Show loading states
    // -----------------------------------------------------

    setHTML(
        "missing-skills-container",
        `
        <div class="state">
            Loading skills...
        </div>
        `
    );


    setHTML(
        "courses-container",
        `
        <div class="state">
            Loading courses...
        </div>
        `
    );


    setHTML(
        "companies-container",
        `
        <div class="state">
            Loading companies...
        </div>
        `
    );


    setHTML(
        "projects-container",
        `
        <div class="state">
            Loading projects...
        </div>
        `
    );


    try {

        // -------------------------------------------------
        // Load all career details simultaneously
        // -------------------------------------------------

        const [
            missingSkills,
            courses,
            companies,
            projects
        ] = await Promise.all([

            fetchAPI(
                `/api/users/${USER_ID}/missing-skills/${career.id}`
            ),

            fetchAPI(
                `/api/users/${USER_ID}/courses/${career.id}`
            ),

            fetchAPI(
                `/api/jobs/${career.id}/companies`
            ),

            fetchAPI(
                `/api/users/${USER_ID}/projects/${career.id}`
            )

        ]);


        // -------------------------------------------------
        // Render each section
        // -------------------------------------------------

        renderMissingSkills(
            missingSkills
        );


        renderCourses(
            courses
        );


        renderCompanies(
            companies
        );


        renderProjects(
            projects
        );

    }

    catch (error) {

        console.error(
            "Unable to load career details:",
            error
        );


        // -------------------------------------------------
        // Show error in every detail section
        // -------------------------------------------------

        setHTML(
            "missing-skills-container",
            `
            <p class="error">
                Unable to load skills.
            </p>
            `
        );


        setHTML(
            "courses-container",
            `
            <p class="error">
                Unable to load courses.
            </p>
            `
        );


        setHTML(
            "companies-container",
            `
            <p class="error">
                Unable to load companies.
            </p>
            `
        );


        setHTML(
            "projects-container",
            `
            <p class="error">
                Unable to load projects.
            </p>
            `
        );
    }
}


// =========================================================
// 8. Render Missing Skills
// =========================================================

function renderMissingSkills(skills) {

    const container =
        document.getElementById(
            "missing-skills-container"
        );


    if (!container) {

        return;
    }


    // -----------------------------------------------------
    // Clear previous content
    // -----------------------------------------------------

    container.innerHTML = "";


    // -----------------------------------------------------
    // Empty state
    // -----------------------------------------------------

    if (!skills || skills.length === 0) {

        container.innerHTML =
            `
            <p class="muted">
                You already have all required skills.
            </p>
            `;

        return;
    }


    // -----------------------------------------------------
    // Render each missing skill
    // -----------------------------------------------------

    for (const skill of skills) {

        const item =
            document.createElement("div");


        item.className =
            "recommendation-item";


        item.innerHTML = `

            <strong>
                ${escapeHTML(skill.name)}
            </strong>


            <span class="badge">
                ${escapeHTML(skill.importance)}
            </span>

        `;


        container.appendChild(item);
    }
}


// =========================================================
// 9. Render Courses
// =========================================================

function renderCourses(courses) {

    const container =
        document.getElementById(
            "courses-container"
        );


    if (!container) {

        return;
    }


    container.innerHTML = "";


    // -----------------------------------------------------
    // Empty state
    // -----------------------------------------------------

    if (!courses || courses.length === 0) {

        container.innerHTML =
            `
            <p class="muted">
                No course recommendations found.
            </p>
            `;

        return;
    }


    // -----------------------------------------------------
    // Render courses
    // -----------------------------------------------------

    for (const course of courses) {

        const item =
            document.createElement("div");


        item.className =
            "recommendation-item";


        item.innerHTML = `

            <div>

                <strong>
                    ${escapeHTML(course.title)}
                </strong>


                <div class="muted">

                    Learn:

                    ${escapeHTML(course.skill)}

                </div>

            </div>

        `;


        container.appendChild(item);
    }
}


// =========================================================
// 10. Render Companies
// =========================================================

function renderCompanies(companies) {

    const container =
        document.getElementById(
            "companies-container"
        );


    if (!container) {

        return;
    }


    container.innerHTML = "";


    // -----------------------------------------------------
    // Empty state
    // -----------------------------------------------------

    if (!companies || companies.length === 0) {

        container.innerHTML =
            `
            <p class="muted">
                No companies found.
            </p>
            `;

        return;
    }


    // -----------------------------------------------------
    // Render companies
    // -----------------------------------------------------

    for (const company of companies) {

        const item =
            document.createElement("div");


        item.className =
            "company-item";


        item.textContent =
            `${company.name} · ${company.industry}`;


        container.appendChild(item);
    }
}


// =========================================================
// 11. Render Projects
// =========================================================

function renderProjects(projects) {

    const container =
        document.getElementById(
            "projects-container"
        );


    if (!container) {

        return;
    }


    container.innerHTML = "";


    // -----------------------------------------------------
    // Empty state
    // -----------------------------------------------------

    if (!projects || projects.length === 0) {

        container.innerHTML =
            `
            <p class="muted">
                No project recommendations found.
            </p>
            `;

        return;
    }


    // -----------------------------------------------------
    // Render projects
    // -----------------------------------------------------

    for (const project of projects) {

        const item =
            document.createElement("article");


        item.className =
            "project-item";


        item.innerHTML = `

            <h4>
                ${escapeHTML(project.title)}
            </h4>


            <p>
                ${escapeHTML(project.description)}
            </p>


            <p>
                Difficulty:
                ${escapeHTML(project.difficulty)}
            </p>


            <p>
                Develops:
                ${escapeHTML(project.skill)}
            </p>

        `;


        container.appendChild(item);
    }
}


// =========================================================
// 12. HTML Escape Helper
// =========================================================
//
// Database values are inserted into HTML in several places.
// Escaping prevents those values from being interpreted as
// HTML markup.
// =========================================================

function escapeHTML(value) {

    if (
        value === null ||
        value === undefined
    ) {

        return "";
    }


    return String(value)

        .replaceAll(
            "&",
            "&amp;"
        )

        .replaceAll(
            "<",
            "&lt;"
        )

        .replaceAll(
            ">",
            "&gt;"
        )

        .replaceAll(
            '"',
            "&quot;"
        )

        .replaceAll(
            "'",
            "&#039;"
        );
}


// =========================================================
// 13. Button Event
// =========================================================

function initializeEventListeners() {

    const button =
        document.getElementById(
            "find-careers-btn"
        );


    if (!button) {

        console.error(
            "Find careers button was not found."
        );

        return;
    }


    button.addEventListener(
        "click",
        loadCareerMatches
    );
}


// =========================================================
// 14. Application Initialization
// =========================================================

document.addEventListener(
    "DOMContentLoaded",
    () => {

        // Load user's existing skills
        loadUserSkills();


        // Initialize button events
        initializeEventListeners();

    }
);