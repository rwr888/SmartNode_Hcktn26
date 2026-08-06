// Configuración centralizada
const CONFIG = {
    API_URL: "http://127.0.0.1:8000/dashboard",
    REFRESH_INTERVAL: 5000 // Actualiza cada 5 segundos
};

/**
 * Actualiza el texto de un elemento del DOM si este existe
 * @param {string} id - ID del elemento HTML
 * @param {string|number} value - Valor a insertar
 */
function updateElementText(id, value) {
    const element = document.getElementById(id);
    if (element) {
        element.textContent = value ?? "0";
    }
}

/**
 * Consulta la API y actualiza la interfaz
 */
async function fetchDashboardData() {
    try {
        const response = await fetch(CONFIG.API_URL);

        // Validar si la respuesta HTTP es exitosa (código 200-299)
        if (!response.ok) {
            throw new Error(`Error en el servidor: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();

        // Mapear los datos de la API a los IDs de las tarjetas
        updateElementText("total-machines", data.total_machines);
        updateElementText("normal-machines", data.normal_machines);
        updateElementText("warning-machines", data.warning_machines);
        updateElementText("critical-machines", data.critical_machines);

    } catch (error) {
        console.error("No se pudieron cargar los datos del dashboard:", error);
        
        // Muestra un estado visual de error en la interfaz
        updateElementText("total-machines", "--");
        updateElementText("normal-machines", "--");
        updateElementText("warning-machines", "--");
        updateElementText("critical-machines", "--");
    }
}

// Inicializar cuando el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", () => {
    // Carga inicial
    fetchDashboardData();

    // Actualización automática en segundo plano (Polling)
    setInterval(fetchDashboardData, CONFIG.REFRESH_INTERVAL);
});

