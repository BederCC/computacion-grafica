// Esperar a que el contenido del DOM se haya cargado
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    form.addEventListener("submit", (event) => {
        // Prevenir el envío del formulario
        event.preventDefault();
        // Mostrar un mensaje de alerta cuando se envíe el formulario
        alert("Formulario enviado!");
    });
});
