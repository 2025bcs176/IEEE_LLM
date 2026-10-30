import markdown, os, subprocess

names = ['literature_review', 'error_analysis', 'recommendation', 'research_report']
os.makedirs('docs/pdf', exist_ok=True)
for name in names:
    md = open(f'docs/{name}.md').read()
    html = markdown.markdown(md, extensions=['tables'])
    full = ('<!DOCTYPE html><html><head><meta charset="utf-8">'
            '<title>' + name + '</title></head><body>' + html + '</body></html>')
    html_path = f'docs/pdf/{name}.html'
    with open(html_path, 'w') as f:
        f.write(full)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf',
                    '--outdir', 'docs/pdf', html_path],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print('created', name + '.pdf')
