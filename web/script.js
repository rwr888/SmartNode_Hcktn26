async function loadDashboard() {

    const response = await fetch("http://127.0.0.1:8000/dashboard");

    const data = await response.json();

    console.log(data);

    document.getElementById("total-machines").textContent =
        data.total_machines;

    document.getElementById("normal-machines").textContent =
        data.normal_machines;

    document.getElementById("warning-machines").textContent =
        data.warning_machines;

    document.getElementById("critical-machines").textContent =
        data.critical_machines;

}

loadDashboard();

