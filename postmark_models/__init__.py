from typing import Any

from .message import MessageInbound as MessageInbound

__version__ = "0.1.2"

example_message: dict[str, Any] = {
    "From": "myUser@theirDomain.com",
    "MessageStream": "inbound",
    "FromName": "My User",
    "FromFull": {
        "Email": "myUser@theirDomain.com",
        "Name": "John Doe",
        "MailboxHash": "",
    },
    "To": "451d9b70cf9364d23ff6f9d51d870251569e+ahoy@inbound.postmarkapp.com",
    "ToFull": [
        {
            "Email": "451d9b70cf9364d23ff6f9d51d870251569e+ahoy@inbound.postmarkapp.com",
            "Name": "",
            "MailboxHash": "ahoy",
        }
    ],
    "Cc": '"Full name" <sample.cc@emailDomain.com>, "Another Cc" <another.cc@emailDomain.com>',
    "CcFull": [
        {"Email": "sample.cc@emailDomain.com", "Name": "Full name", "MailboxHash": ""},
        {
            "Email": "another.cc@emailDomain.com",
            "Name": "Another Cc",
            "MailboxHash": "",
        },
    ],
    "Bcc": '"Full name" <451d9b70cf9364d23ff6f9d51d870251569e@inbound.postmarkapp.com>',
    "BccFull": [
        {
            "Email": "451d9b70cf9364d23ff6f9d51d870251569e@inbound.postmarkapp.com",
            "Name": "Full name",
            "MailboxHash": "",
        }
    ],
    "OriginalRecipient": "451d9b70cf9364d23ff6f9d51d870251569e+ahoy@inbound.postmarkapp.com",
    "ReplyTo": "myUsersReplyAddress@theirDomain.com",
    "Subject": "This is an inbound message",
    "MessageID": "22c74902-a0c1-4511-804f-341342852c90",
    "Date": "Thu, 5 Apr 2012 16:59:01 +0200",
    "MailboxHash": "ahoy",
    "TextBody": "[ASCII]",
    "HtmlBody": "[HTML]",
    "StrippedTextReply": "Ok, thanks for letting me know!",
    "Tag": "",
    "Headers": [
        {
            "Name": "X-Spam-Checker-Version",
            "Value": "SpamAssassin 3.3.1 (2010-03-16) onrs-ord-pm-inbound1.wildbit.com",
        },
        {"Name": "X-Spam-Status", "Value": "No"},
        {"Name": "X-Spam-Score", "Value": "-0.1"},
        {
            "Name": "X-Spam-Tests",
            "Value": "DKIM_SIGNED,DKIM_VALID,DKIM_VALID_AU,SPF_PASS",
        },
        {
            "Name": "Received-SPF",
            "Value": "Pass (sender SPF authorized) identity=mailfrom; client-ip=209.85.160.180; helo=mail-gy0-f180.google.com; envelope-from=myUser@theirDomain.com; receiver=451d9b70cf9364d23ff6f9d51d870251569e+ahoy@inbound.postmarkapp.com",
        },
        {
            "Name": "DKIM-Signature",
            "Value": "v=1; a=rsa-sha256; c=relaxed/relaxed;        d=wildbit.com; s=google;        h=mime-version:reply-to:message-id:subject:from:to:cc         :content-type;        bh=cYr/+oQiklaYbBJOQU3CdAnyhCTuvemrU36WT7cPNt0=;        b=QsegXXbTbC4CMirl7A3VjDHyXbEsbCUTPL5vEHa7hNkkUTxXOK+dQA0JwgBHq5C+1u         iuAJMz+SNBoTqEDqte2ckDvG2SeFR+Edip10p80TFGLp5RucaYvkwJTyuwsA7xd78NKT         Q9ou6L1hgy/MbKChnp2kxHOtYNOrrszY3JfQM=",
        },
        {"Name": "MIME-Version", "Value": "1.0"},
        {
            "Name": "Message-ID",
            "Value": "<CAGXpo2WKfxHWZ5UFYCR3H_J9SNMG+5AXUovfEFL6DjWBJSyZaA@mail.gmail.com>",
        },
    ],
    "Attachments": [
        {
            "Name": "myimage.png",
            "Content": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCAAwADADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDg7nQ9XlmtLWPTbku9wg5jIA5zknsPevbvBXhjTdPRXvJUubleW5+RT7D+prlRq32WFpWb5+w9qzrTxFMrqyySlyMhR1J/Dmvl62aNyUGtArNqXLE9+tNSs4IFRpB6cdfpWX4slsdQszGzblUhlZTgow6Mp9Qa8lXxFqEeQ0bRrkACVtgyfYkUsmu3sbhneHDHgeepz9eaueLpyp8ljD2VTojSuLhNQeWz1FwL+3+5Oox5qdmI/nWDdu0bPC55U4NUp9Tkn1aGSMoZERg21wfl69vxrT0fTpPEV61skyx3WwtFu4D46g+9eLWwbrNKC978z0sFiJUXyVNvyOR1q4un1E2sTFV3Dn2xzVPxN4qbwwZoI7Ca5iwpMm8ouCDnBHNb99FG80h2jcQPyq9p+lQanb7poEkOMHcM9AAQfyruwc4OpaSuPl/eNI47Rtf0DxKkV4iNFcQuu+OX1/vA/wAQ7ZFHjrxNc6fbQWfh+wM9wSz7kiL+SvQHb6nP6VoeJfDjxTi80i1U/ZQdwGApXHIAHXFS+EdNuJ7U6vfwqUuiDHsJ3bBwMg/nXalBS5re72OhwbjYzfAEfiImK91i6maWSVd8WFVQp4xwOeDzXXeE79tO8W2xHL293sI/2Twf0JrVuLa1t7FZFUgLgjjvmuZmRk8bXAU9HLfjsJrGtUftIzRxV4bF+ewvjI0hsZyFPeM4xT7HUlsLS6OGKqpfjqB3rqvFOszaZZkQ8tIhB78e3vXl15qpgnWGGPDj5pFJyCT2zWMMHKmlNanRUfNLmOl0nVbTW7XYsvkRHtnDGpgINKgCQXO4AdCcjFc5p9iNzTonlbuVQnpV9bIRQt50oZic5zx+FdShJo1UtCZtTfUNXsrN+I3cMwHcDn+lJApk8QXt86OyKG5UZxngH8s0y3gjF0bu3kTzQhVQTwuRjNa/hieDS4/MEglcH98c/eHfHtRTpKVVKWyOetG7uj//2Q==",
            "ContentType": "image/png",
            "ContentLength": 4096,
            "ContentID": "myimage.png@01CE7342.75E71F80",
        },
        {
            "Name": "mypaper.doc",
            "Content": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCAAwADADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDg7nQ9XlmtLWPTbku9wg5jIA5zknsPevbvBXhjTdPRXvJUubleW5+RT7D+prlRq32WFpWb5+w9qzrTxFMrqyySlyMhR1J/Dmvl62aNyUGtArNqXLE9+tNSs4IFRpB6cdfpWX4slsdQszGzblUhlZTgow6Mp9Qa8lXxFqEeQ0bRrkACVtgyfYkUsmu3sbhneHDHgeepz9eaueLpyp8ljD2VTojSuLhNQeWz1FwL+3+5Oox5qdmI/nWDdu0bPC55U4NUp9Tkn1aGSMoZERg21wfl69vxrT0fTpPEV61skyx3WwtFu4D46g+9eLWwbrNKC978z0sFiJUXyVNvyOR1q4un1E2sTFV3Dn2xzVPxN4qbwwZoI7Ca5iwpMm8ouCDnBHNb99FG80h2jcQPyq9p+lQanb7poEkOMHcM9AAQfyruwc4OpaSuPl/eNI47Rtf0DxKkV4iNFcQuu+OX1/vA/wAQ7ZFHjrxNc6fbQWfh+wM9wSz7kiL+SvQHb6nP6VoeJfDjxTi80i1U/ZQdwGApXHIAHXFS+EdNuJ7U6vfwqUuiDHsJ3bBwMg/nXalBS5re72OhwbjYzfAEfiImK91i6maWSVd8WFVQp4xwOeDzXXeE79tO8W2xHL293sI/2Twf0JrVuLa1t7FZFUgLgjjvmuZmRk8bXAU9HLfjsJrGtUftIzRxV4bF+ewvjI0hsZyFPeM4xT7HUlsLS6OGKqpfjqB3rqvFOszaZZkQ8tIhB78e3vXl15qpgnWGGPDj5pFJyCT2zWMMHKmlNanRUfNLmOl0nVbTW7XYsvkRHtnDGpgINKgCQXO4AdCcjFc5p9iNzTonlbuVQnpV9bIRQt50oZic5zx+FdShJo1UtCZtTfUNXsrN+I3cMwHcDn+lJApk8QXt86OyKG5UZxngH8s0y3gjF0bu3kTzQhVQTwuRjNa/hieDS4/MEglcH98c/eHfHtRTpKVVKWyOetG7uj//2Q==",
            "ContentType": "application/msword",
            "ContentLength": 16384,
            "ContentID": "",
        },
    ],
}
