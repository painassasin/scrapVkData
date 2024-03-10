import re
from datetime import datetime

import dateparser
from pydantic import BaseModel
from typing_extensions import Self

DATE_PATTERNS = (
    re.compile(r'at\s(?P<time>[\d\:]+\s(am|pm))\son\s(?P<date>[\d]{1,2}\s[\w]+\s[\d]{4})'),
    re.compile(r'(?P<date>\d{1,2}\s[а-я]+\s\d{4})\sв\s(?P<time>\d{1,2}:\d{2}:\d{2})'),
)


class Image(BaseModel):
    link: str
    sent_at: datetime

    @classmethod
    def from_link_and_header(cls, link: str, header: str) -> Self:
        result = None

        for pattern in DATE_PATTERNS:
            result = pattern.search(header)
            if result:
                break

        if result:
            result_dict = result.groupdict()
            send_at = dateparser.parse(f"{result_dict['date']} {result_dict['time']}")
            if send_at:
                return cls(link=link, sent_at=send_at)

        raise ValueError(f'Failed to parse date from header: {header}')
