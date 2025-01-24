def markdown_to_blocks(markdown):
    # Split the markdown text into blocks based on empty lines
    blocks = markdown.split("\n\n")
    
    # Process each block
    result = []
    for block in blocks:
        # Strip whitespace and skip empty blocks
        cleaned_block = block.strip()
        if cleaned_block:  # Only add non-empty blocks
            result.append(cleaned_block)
            
    return result