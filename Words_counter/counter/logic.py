from typing import Union

import PyPDF2
import docx


def count_words_in_pdf(file_path: str) -> Union[dict[str, int], str]:
    try:
        # with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(file_path)
        total_words = 0
        total_unique_words = 0

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            words = text.split()
            unique_words = set(text.split())
            total_words += len(words)
            total_unique_words += len(unique_words)

        return {'total_words': total_words, 'unique_words': total_unique_words}
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)


def count_words_in_docx(file_path):
    try:
        doc = docx.Document(file_path)
        total_words = 0
        total_unique_words = 0

        for paragraph in doc.paragraphs:
            words = paragraph.text.split()
            unique_words = set(paragraph.text.split())
            total_words += len(words)
            total_unique_words += len(unique_words)

        return {'total_words': total_words, 'unique_words': total_unique_words}
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)