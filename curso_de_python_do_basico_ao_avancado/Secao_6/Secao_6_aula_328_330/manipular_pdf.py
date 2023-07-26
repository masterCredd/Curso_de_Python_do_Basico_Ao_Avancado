from pathlib import Path

from PyPDF2 import PdfFileMerger, PdfReader, PdfFileWriter, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'dados_pdf'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230303.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

print(len(reader.pages))

# for page in reader.pages
#     print(page)
#     print()

page_0 = reader.pages[0]
imagem_0 = page_0.images[0]

# print(page_0.extract_text())
# with open(PASTA_NOVA / imagem_0.name, 'wb') as fp:
#     fp.write(imagem_0.data)


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)
        

files = [
    PASTA_NOVA/'page1.pdf',
    PASTA_NOVA/'page0.pdf',
]

merger = PdfFileMerger()
for file in files:
    merger.append(file)
    

merger.write(PASTA_NOVA/'MERGED.pdf')
merger.close()