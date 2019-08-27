import subprocess

filename = "1901.00686"
subprocess.run(["pdf2txt.py", "-o", "output.txt", "-p", "1", filename+".pdf"])
with open("output.txt", "r", encoding="utf-8") as f:
    txt = f.readlines()
    print(filename)
    print("https://arxiv.org/pdf/"+filename+".pdf")
    cnt = 0
    for line in txt:
        line = line.lower()
        show_line = False
        if len(line) >5:
            cnt += 1
            show_line = True
        if cnt <= 20 or "univer" in line or 'institu' in line or 'college' in line or 'school' in line:
            if show_line:
                print(line.encode('utf-8'))
