def block_to_block_type(block):
    # Check for code blocks
    if block.startswith("```") and block.endswith("```"):
        return "code"

    # Split into lines for multi-line block analysis
    lines = block.split("\n")
    first_line = lines[0]

    # Check for headings (1-6 # characters followed by a space)
    if first_line.startswith("#"):
        for i in range(6, 0, -1):
            if first_line.startswith("#" * i + " "):
                return "heading"

    # Check for quote blocks (every line must start with >)
    if all(line.startswith(">") for line in lines):
        return "quote"

    # Check for unordered lists (every line must start with * or -)
    if all(line.strip().startswith(("* ", "- ")) for line in lines):
        return "unordered_list"

    # Check for ordered lists (must start with 1 and increment)
    if all(line.strip().startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return "ordered_list"

    # Default to paragraph if no other type matches
    return "paragraph"