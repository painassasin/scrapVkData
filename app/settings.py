from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

HTML_FILES_PATTERN = '**/*.html'
OUT_DIR = BASE_DIR.joinpath('out')
IN_DIR = BASE_DIR.joinpath('messages')
DIV_ATTACHMENT_CLASS = 'attachment__description'
LINK_ATTACHMENT_CLASS = 'attachment__link'
MESSAGE_HEADER_CLASS = 'message__header'
