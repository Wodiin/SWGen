from enum import Enum


class BlockType (Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNLIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
        hash_count = 0
        for letter in block:
            if letter == "#":
                hash_count += 1
            else:
                break
        if hash_count > 0 and hash_count <= 6 and block[hash_count:hash_count+1] == " ":
            return BlockType.HEADING
        if block.startswith("```\n") and block.endswith("```"):
            return BlockType.CODE
        split_block = block.split("\n")
        if all(line.startswith(">") for line in split_block):
            return BlockType.QUOTE
        if all(line.startswith("- ") for line in split_block):
            return BlockType.UNLIST
        if all(line.startswith(f"{i}. ") for i, line in enumerate(split_block, start=1)):
            return BlockType.OLIST
        return BlockType.PARAGRAPH