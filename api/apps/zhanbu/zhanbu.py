import random

def generate_hexagram():
    """生成易经卦象，返回本卦和变卦信息"""
    # 八卦映射表（下、中、上爻）,从下往上排
    trigram_map = {
        (1, 1, 1): '乾',
        (1, 1, 0): '兑',
        (1, 0, 1): '离',
        (1, 0, 0): '震',
        (0, 1, 1): '巽',
        (0, 1, 0): '坎',
        (0, 0, 1): '艮',
        (0, 0, 0): '坤',
    }
    hexagram_map = {
        # 上经三十卦（1-30）
        ('乾', '乾'): {'name': '乾为天', 'number': 1},
        ('坤', '坤'): {'name': '坤为地', 'number': 2},
        ('震', '坎'): {'name': '水雷屯', 'number': 3},      # 下震上坎 ✔
        ('坎', '艮'): {'name': '山水蒙', 'number': 4},      # 下坎上艮 ✔
        ('乾', '坎'): {'name': '水天需', 'number': 5},      # 下乾上坎 ✔
        ('坎', '乾'): {'name': '天水讼', 'number': 6},      # 下坎上乾 ✔
        ('坎', '坤'): {'name': '地水师', 'number': 7},      # 下坎上坤 ✔
        ('坤', '坎'): {'name': '水地比', 'number': 8},      # 下坤上坎 ✔
        ('乾', '巽'): {'name': '风天小畜', 'number': 9},    # 下乾上巽 ✔
        ('兑', '乾'): {'name': '天泽履', 'number': 10},     # 下兑上乾 ✔
        ('乾', '坤'): {'name': '地天泰', 'number': 11},     # 下乾上坤 ✔
        ('坤', '乾'): {'name': '天地否', 'number': 12},     # 下坤上乾 ✔
        ('离', '乾'): {'name': '天火同人', 'number': 13},   # 下离上乾 ✔
        ('乾', '离'): {'name': '火天大有', 'number': 14},   # 下乾上离 ✔
        ('艮', '坤'): {'name': '地山谦', 'number': 15},     # 下艮上坤 ✔
        ('坤', '震'): {'name': '雷地豫', 'number': 16},     # 下坤上震 ✔
        ('震', '兑'): {'name': '泽雷随', 'number': 17},     # 下震上兑 ✔
        ('巽', '艮'): {'name': '山风蛊', 'number': 18},     # 下巽上艮 ✔
        ('兑', '坤'): {'name': '地泽临', 'number': 19},     # 下兑上坤 ✔
        ('坤', '巽'): {'name': '风地观', 'number': 20},     # 下坤上巽 ✔
        ('震', '离'): {'name': '火雷噬嗑', 'number': 21},   # 下震上离 ✔
        ('离', '艮'): {'name': '山火贲', 'number': 22},     # 下离上艮 ✔
        ('坤', '艮'): {'name': '山地剥', 'number': 23},     # ✨ 修正：原错误为 ('艮','坤')
        ('震', '坤'): {'name': '地雷复', 'number': 24},     # ✨ 修正：原错误为 ('坤','震')
        ('震', '乾'): {'name': '天雷无妄', 'number': 25},   # 下震上乾 ✔
        ('乾', '艮'): {'name': '山天大畜', 'number': 26},   # 下乾上艮 ✔
        ('震', '艮'): {'name': '山雷颐', 'number': 27},     # 下震上艮 ✔
        ('巽', '兑'): {'name': '泽风大过', 'number': 28},   # 下巽上兑 ✔
        ('坎', '坎'): {'name': '坎为水', 'number': 29},     # 下坎上坎 ✔
        ('离', '离'): {'name': '离为火', 'number': 30},     # 下离上离 ✔

        # 下经三十四卦（31-64）
        ('艮', '兑'): {'name': '泽山咸', 'number': 31},     # 下艮上兑 ✔
        ('巽', '震'): {'name': '雷风恒', 'number': 32},     # 下巽上震 ✔
        ('艮', '乾'): {'name': '天山遁', 'number': 33},     # 下艮上乾 ✔
        ('乾', '震'): {'name': '雷天大壮', 'number': 34},   # 下乾上震 ✔
        ('坤', '离'): {'name': '火地晋', 'number': 35},     # 下坤上离 ✔
        ('离', '坤'): {'name': '地火明夷', 'number': 36},   # 下离上坤 ✔
        ('离', '巽'): {'name': '风火家人', 'number': 37},   # 下离上巽 ✔
        ('兑', '离'): {'name': '火泽睽', 'number': 38},     # 下兑上离 ✔
        ('艮', '坎'): {'name': '水山蹇', 'number': 39},     # ✨ 修正：原错误为 ('坎','艮')
        ('坎', '震'): {'name': '雷水解', 'number': 40},     # ✨ 修正：原错误为 ('震','坎')
        ('兑', '艮'): {'name': '山泽损', 'number': 41},     # ✨ 修正：原错误为 ('艮','兑')
        ('震', '巽'): {'name': '风雷益', 'number': 42},     # ✨ 修正：原错误为 ('巽','震')
        ('兑', '乾'): {'name': '泽天夬', 'number': 43},     # 下兑上乾 ✔
        ('乾', '巽'): {'name': '天风姤', 'number': 44},     # 下乾上巽 ✔
        ('兑', '坤'): {'name': '地泽萃', 'number': 45},     # 下兑上坤 ✔
        ('坤', '巽'): {'name': '风地升', 'number': 46},     # 下坤上巽 ✔
        ('坎', '兑'): {'name': '泽水困', 'number': 47},     # 下坎上兑 ✔
        ('巽', '坎'): {'name': '水风井', 'number': 48},     # 下巽上坎 ✔
        ('离', '兑'): {'name': '泽火革', 'number': 49},    # 下离上兑 ✔
        ('巽', '离'): {'name': '火风鼎', 'number': 50},     # 下巽上离 ✔
        ('震', '震'): {'name': '震为雷', 'number': 51},     # 下震上震 ✔
        ('艮', '艮'): {'name': '艮为山', 'number': 52},     # 下艮上艮 ✔
        ('艮', '巽'): {'name': '风山渐', 'number': 53},     # ✨ 修正：原错误为 ('巽','艮')
        ('兑', '震'): {'name': '雷泽归妹', 'number': 54},   # ✨ 修正：原错误为 ('震','兑')
        ('离', '震'): {'name': '雷火丰', 'number': 55},     # 下离上震 ✔
        ('艮', '离'): {'name': '火山旅', 'number': 56},     # 下艮上离 ✔
        ('巽', '巽'): {'name': '巽为风', 'number': 57},     # 下巽上巽 ✔
        ('兑', '兑'): {'name': '兑为泽', 'number': 58},     # 下兑上兑 ✔
        ('坎', '巽'): {'name': '风水涣', 'number': 59},     # 下坎上巽 ✔
        ('兑', '坎'): {'name': '水泽节', 'number': 60},     # 下兑上坎 ✔
        ('兑', '巽'): {'name': '风泽中孚', 'number': 61},   # ✨ 修正：原错误为 ('巽','兑')
        ('艮', '震'): {'name': '雷山小过', 'number': 62},   # ✨ 修正：原错误为 ('震','艮')
        ('离', '坎'): {'name': '水火既济', 'number': 63},   # 下离上坎 ✔
        ('坎', '离'): {'name': '火水未济', 'number': 64},   # 下坎上离 ✔
    }

    # 生成六个爻
    original_yaos = []
    moving_flags = []
    
    # 生成每个爻
    for _ in range(6):
        # 抛三次硬币
        coins = []
        for _ in range(3):
            coins.append(random.choice([2, 3]))
        total = sum(coins)

        # 判断爻象
        if total == 6:  # 老阴（动爻）
            original_yaos.append(0)
            moving_flags.append(True)
        elif total == 7:  # 少阳
            original_yaos.append(1)
            moving_flags.append(False)
        elif total == 8:  # 少阴
            original_yaos.append(0)
            moving_flags.append(False)
        elif total == 9:  # 老阳（动爻）
            original_yaos.append(1)
            moving_flags.append(True)

    # 生成变卦
    changed_yaos = []
    for i in range(len(original_yaos)):
        yao = original_yaos[i]
        flag = moving_flags[i]
        if flag:
            changed_yaos.append(1 - yao)
        else:
            changed_yaos.append(yao)
            
    # 查找动爻位置
    moving_positions = []
    for index, flag in enumerate(moving_flags):
        if flag:
            moving_positions.append(index + 1)  # 爻位从1开始计数

    # 获取八卦名称
    def get_trigram(yaos):
        #之前得到的结果是由下往上的，现在计算卦名是由上往下的，所以要反向排序
        key = (yaos[0], yaos[1], yaos[2])
        return trigram_map.get(key, "未知")
    
    def get_64gua(t: tuple):
        name_64gua = hexagram_map.get(t)["name"]
        return name_64gua

    # 组合卦象信息
    result = {
        'bengua': {
            'gua': get_64gua((get_trigram(original_yaos[0:3]),get_trigram(original_yaos[3:6]))),
            'yao': original_yaos,
            'xiagua': get_trigram(original_yaos[0:3]),
            'shanggua': get_trigram(original_yaos[3:6]),
            'dongyao': moving_positions,
        },
        'biangua': {
            'gua': get_64gua((get_trigram(changed_yaos[0:3]),get_trigram(changed_yaos[3:6]))),
            'yao': changed_yaos,
            'xiagua': get_trigram(changed_yaos[0:3]),
            'shanggua': get_trigram(changed_yaos[3:6]),
        }
    }
    return result

def print_hexagram(info):
    """打印卦象信息"""
    # 转换本卦符号
    original_symbols = []
    for yao in info['original']['yaos']:
        original_symbols.append(str(yao))
    original_symbols = ' '.join(original_symbols)

    # 转换变卦符号
    changed_symbols = []
    for yao in info['changed']['yaos']:
        changed_symbols.append(str(yao))
    changed_symbols = ' '.join(changed_symbols)

    # 查找动爻位置
    moving_positions = []
    for index, flag in enumerate(info['original']['moving']):
        if flag:
            moving_positions.append(index + 1)  # 爻位从1开始计数

    # 打印结果
    print("本卦组成：")
    print(f"卦名（64卦）：{info['original']['gua_name']}")
    print(f"下卦：{info['original']['lower']}，上卦：{info['original']['upper']}")
    print("爻象（从下到上）：", original_symbols)
    print("动爻位置：", moving_positions)

    print("\n变卦组成：")
    print(f"卦名（64卦）：{info['changed']['gua_name']}")
    print(f"下卦：{info['changed']['lower']}，上卦：{info['changed']['upper']}")
    print("爻象（从下到上）：", changed_symbols)

if __name__ == "__main__":
    hexagram_info = generate_hexagram()
    print_hexagram(hexagram_info)
