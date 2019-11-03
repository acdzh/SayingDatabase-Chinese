

if __name__ == "__main__":
    with open('data.txt', encoding='utf-8') as f:
        for line in f.readlines()[0:4]:
            line = line.strip()
            a = line.find('$$')
            b = line.find('$$', a + 2)
            name = line[a + 2: b]
            saying = line[b + 2 : ]
            print (name, saying)
