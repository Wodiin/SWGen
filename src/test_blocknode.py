import unittest

from blocknode import BlockType, block_to_block_type

class TestBlockNode(unittest.TestCase):
    def test_block_type(self):
        self.assertEqual(BlockType.PARAGRAPH.value, "paragraph")
        self.assertEqual(BlockType.HEADING.value, "heading")
        self.assertEqual(BlockType.CODE.value, "code")
        self.assertEqual(BlockType.QUOTE.value, "quote")
        self.assertEqual(BlockType.UNLIST.value, "unordered_list")
        self.assertEqual(BlockType.OLIST.value, "ordered_list")
    
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```\nCode block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> Quote\n> Line 2"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNLIST)
        self.assertEqual(block_to_block_type("1. First\n2. Second"), BlockType.OLIST)