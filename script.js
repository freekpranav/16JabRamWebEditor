function runCode() {
    const code = document.getElementById('editor').value;
    const outputDiv = document.getElementById('output');

    try {
        // Simulate execution with a timeout
        setTimeout(() => {
            const result = executeCode(code);
            outputDiv.innerText = result;
        }, 500);
    } catch (error) {
        outputDiv.innerText = `Error: ${error.message}`;
    }
}

function executeCode(code) {
    // In a real environment, you would execute the code here.
    // For simplicity, let's just return the code itself.
    return code;
}
