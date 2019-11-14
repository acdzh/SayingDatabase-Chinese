def isNameValid(name):
    test_set = [
        "《", "（", "(", "【", "，", "。", ",", ".", "[", "_","、", "\\", "．", "’", "‘", "'","-",
        "法", "意大利", "保加利亚", "俄", "西班牙", "国", "族", "家", "奥地利", "朝鲜", "埃及", "土耳其", "越南", "苏联", "西方", "日本", 
        "洲", "荷兰", "台湾", "印尼", "铒印度尼亚", "蒙古",  "老挝", "罗马尼亚", "巴基斯坦", "波萨尼亚", "匈牙利", "马来西亚", "丹麦", "言", 
        "记者",  "谚",  "CEO", "的", "座右铭", "未知", "佚", "社", "水浒", "水浒传", "史", "法", "员", "阿富汗", "书", "天才", "大学", 
        "校", "需要", "训", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "首", "蝉", "总", "词", "话", "要", "本草纲目", "总", "唐", "晋",  "志当存高远",  "无名", "老鹰不孵斑鸠", "她", "他", "它", "资治通鉴", "弟子", 
        "文", "三字经", "唯有真诚识真诚", "活着就意味着思考", "奥运会口号", "小学", "中论", "二者不可得", "语", "杭州", "西游记", "红楼梦", "春秋", 
        "金条才有理", "强学力行", "思想就是力量", "阿尔及利亚", "黄帝经", "论", "美是美德之花", "画说生意经", "鹦鹉坚定", "永守重信", "叙利亚", 
        "今道友信", "小坑", "领导科学基础", "武者小路实笃", "习惯成自然", "习俗是暴君", "诗经", "柬埔寨", "兵贵神速", "欧里庇得斯监狱", "阿根廷", 
        "集团", "土耳其", "尼泊尔", "猴子", "印度", "古巴", "瑞士", "机构", "机关", "以德育为先", "葡萄牙", "通鉴", "苏丹", "语录", "摘", 
        "戴东原先生手谱", "周易", "伊朗"
    ]
    for test_str in test_set:
        if test_str in name:
            # print(test_str)
            return False
    return True

isNameValid('马可·奥勒留')

if __name__ == "__main__":
    
    logion_sentence = [] # 用于保存并筛选名人名言
    
    # 拿到纯净的人名
    with open('data.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            a = line.find('$$')
            b = line.find('$$', a + 2)
            name = line[a + 2: b]
            logion = line[b + 2 : ]
            logion_sentence.append({
                "name": name,
                "logion": logion,
                "valid": isNameValid(name)
            })
    
    with open('data_clean.txt', 'w', encoding='utf-8') as f:
        with open('data_dirty.txt', 'w', encoding='utf-8') as g:
            for s in logion_sentence:
                if s["valid"]:
                    f.write(f'{s["name"]}$${s["logion"]}\n')
                else:
                    g.write(f'{s["name"]}$${s["logion"]}\n')
        
        

