

if __name__ == "__main__":
    
    logion_sentence = [] # 用于保存并筛选名人名言
    name_set = set() # 拿到所有人名，便于手工剔除书名、佚名等无用作者
    
    # 拿到纯净的人名
    with open('data.txt', 'e', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            a = line.find('$$')
            b = line.find('$$', a + 2)
            name = line[a + 2: b]
            name_set.add(name)
        
        name_list = list(name_set)
        dirty_name = [] # 不可用的名字
        clean_name = [] # 纯净可用的名字

        # 把非人名存入 dirty_name 中，把纯净人名存入 clean_name 中
        for people_name in name_set:
            if "《" in people_name or "（" in people_name or "(" in people_name or "【" in people_name \
            or "，" in people_name or "。" in people_name or "," in people_name or "." in people_name \
            or "[" in people_name or "·" in people_name or "法" in people_name or "意大利" in people_name\
            or "水浒传" in people_name or "保加利亚" in people_name or "族" in people_name or "言" in people_name\
            or "记者" in people_name or "俄" in people_name or "谚" in people_name or "_" in people_name\
            or "CEO" in people_name or "家" in people_name or "国" in people_name or "西班牙" in people_name\
            or "的" in people_name or "座右铭" in people_name or "未知" in people_name or "佚" in people_name\
            or "奥地利" in people_name or "社" in people_name or "日本" in people_name or "水浒" in people_name\
            or "史" in people_name or "人" in people_name or "法" in people_name or "员" in people_name \
            or "阿富汗" in people_name or "苏联" in people_name or "西方" in people_name or "书" in people_name \
            or "土耳其" in people_name or "越南" in people_name or "天才" in people_name or "洲" in people_name \
            or "埃及" in people_name or "大学" in people_name or "朝鲜" in people_name or "校" in people_name \
            or "需要" in people_name or "荷兰" in people_name or "台湾" in people_name or "训" in people_name\
            or "1" in people_name or "2" in people_name or "3" in people_name or "4" in people_name\
            or "5" in people_name or "6" in people_name or "7" in people_name or "8" in people_name\
            or "9" in people_name or "0" in people_name or "首" in people_name or "蝉" in people_name\
            or "总" in people_name or "词" in people_name or "话" in people_name or "要" in people_name\
            or "本草纲目" in people_name or "总" in people_name or "董" in people_name or "歌" in people_name\
            or "唐" in people_name or "宋" in people_name or "元" in people_name or "明" in people_name\
            or "清" in people_name or "晋" in people_name or "魏" in people_name or "’" in people_name\
            or "‘" in people_name or "'" in people_name or "志当存高远" in people_name or "．" in people_name\
            or "无名" in people_name or "老鹰不孵斑鸠" in people_name or "她" in people_name or "他" in people_name\
            or "它" in people_name or "资治通鉴" in people_name or "弟子" in people_name or "文" in people_name\
            or "三字经" in people_name or "土耳其" in people_name or "唯有真诚识真诚" in people_name or "活着就意味着思考" in people_name\
            or "奥运会口号" in people_name or "小学" in people_name or "、" in people_name or "\\" in people_name\
            or "中论" in people_name or "二者不可得" in people_name or "印尼" in people_name or "铒印度尼亚" in people_name\
            or "蒙古" in people_name or "-" in people_name or "老挝" in people_name or "语" in people_name\
            or "杭州" in people_name or "西游记" in people_name or "红楼梦" in people_name or "春秋" in people_name\
            or "金条才有理" in people_name or "强学力行" in people_name or "罗马尼亚" in people_name or "巴基斯坦" in people_name\
            or "波萨尼亚" in people_name or "匈牙利" in people_name or "马来西亚" in people_name or "丹麦" in people_name\
            or "思想就是力量" in people_name or "阿尔及利亚" in people_name or "黄帝经" in people_name or "论" in people_name\
            or "美是美德之花" in people_name or "画说生意经" in people_name or "鹦鹉坚定" in people_name or "永守重信" in people_name\
            or "叙利亚" in people_name or "今道友信" in people_name or "小坑" in people_name or "领导科学基础" in people_name\
            or "武者小路实笃" in people_name or "习惯成自然" in people_name or "习俗是暴君" in people_name or "诗经" in people_name\
            or "柬埔寨" in people_name or "兵贵神速" in people_name or "欧里庇得斯监狱" in people_name or "阿根廷" in people_name\
            or "集团" in people_name or "土耳其" in people_name or "尼泊尔" in people_name or "猴子" in people_name\
            or "印度" in people_name or "古巴" in people_name or "瑞士" in people_name or "机构" in people_name\
            or "机关" in people_name or "以德育为先" in people_name or "葡萄牙" in people_name or "通鉴" in people_name\
            or "苏丹" in people_name or "亚" in people_name or "语录" in people_name or "摘" in people_name\
            or "戴东原先生手谱" in people_name or "周易" in people_name or "伊朗" in people_name:
                dirty_name.append(people_name)
            else:
                clean_name.append(people_name)
    
    # 拿到纯净的句子
    with open('data.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            a = line.find('$$')
            b = line.find('$$', a + 2)
            name = line[a + 2: b]
            saying = line[b + 2 : ]
            if name in clean_name:
                logion_sentence.append(name + 'a，' + saying + 'b')
            
    # 写入 logion.txt 文件中
    with open('logion.txt','a',encoding='utf-8') as fi:
        for temp_sentence in logion_sentence:
            fi.write("{}".format(temp_sentence) + '\n')