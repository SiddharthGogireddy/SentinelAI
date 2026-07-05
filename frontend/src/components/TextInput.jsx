function TextInput({ text, setText }) {
    return (
        <textarea
            rows="15"
            cols="80"
            placeholder="Paste a Privacy Policy or Terms of Service..."
            value={text}
            onChange={(e) => setText(e.target.value)}
        />
    );
}

export default TextInput;