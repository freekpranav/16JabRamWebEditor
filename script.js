document.addEventListener('DOMContentLoaded', function () {
    const editor = document.getElementById('editor');

    editor.addEventListener('input', function () {
        // Handle text changes here
        const content = editor.innerHTML;
        console.log(content);
    });
});
