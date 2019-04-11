# -*- coding: UTF-8 -*-
import frontmatter
import logging


def read_frontmatter(path):

    post = frontmatter.load(path)
    print(post.metadata)
    #logging.info("read frontmatter : " , post.content())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    read_frontmatter("E:/WorkSpace/page/my_blog/CSBasics/概率论与数理统计/概率论与数理统计(1).md")
