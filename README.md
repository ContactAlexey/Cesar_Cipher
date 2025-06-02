<h1>Caesar Cipher Encryptor (Tkinter GUI)</h1>

<h2>Description</h2>
    <p>This is a simple Python GUI application using <strong>Tkinter</strong> that implements the <em>Caesar Cipher</em>. 
    You can input text and a shift key (integer), and it will output the encrypted text based on the Caesar Cipher algorithm.</p>

  <h2>How to Use</h2>
    <ol>
        <li>Run the Python script.</li>
        <li>Enter the text you want to encrypt.</li>
        <li>Enter the shift value (a positive or negative integer).</li>
        <li>Click the <strong>Encrypt</strong> button.</li>
        <li>The encrypted result will be shown below.</li>
    </ol>

  <h2>Caesar Cipher Function</h2>
    <pre><code>def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + k) % 26 + ascii_offset)
        else:
            result += char
    return result
</code></pre>

  <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>No external libraries required (uses built-in <code>tkinter</code> and <code>ttk</code>)</li>
    </ul>

  <h2>Preview</h2>
    <p>(You can insert a screenshot of the GUI here)</p>

  <h2>Author</h2>
    <p>Made with Python and Tkinter</p>
