from lunar_python import Solar, Lunar
from datetime import datetime




async def calculate_shishen(bazi_list: list)->list:

    # 天干五行和阴阳属性
    GAN_WUXING = {'甲': '木', '乙': '木', '丙': '火', '丁': '火', '戊': '土', '己': '土', '庚': '金', '辛': '金', '壬': '水', '癸': '水'}
    GAN_YINYANG = {'甲': '阳', '乙': '阴', '丙': '阳', '丁': '阴', '戊': '阳', '己': '阴', '庚': '阳', '辛': '阴', '壬': '阳', '癸': '阴'}


    # 十神关系表（基于日干五行和阴阳）
    SHISHEN_RELATION = {
        '水': {
            '水': {'阳': '比肩', '阴': '劫财'},  # 同我
            '金': {'阳': '偏印', '阴': '正印'},  # 生我
            '木': {'阳': '食神', '阴': '伤官'},  # 我生
            '火': {'阳': '偏财', '阴': '正财'},  # 我克
            '土': {'阳': '七杀', '阴': '正官'}   # 克我
        },
        '木': {
            '木': {'阳': '比肩', '阴': '劫财'},
            '水': {'阳': '偏印', '阴': '正印'},
            '火': {'阳': '食神', '阴': '伤官'},
            '土': {'阳': '偏财', '阴': '正财'},
            '金': {'阳': '七杀', '阴': '正官'}
        },
        '火': {
            '火': {'阳': '比肩', '阴': '劫财'},
            '木': {'阳': '偏印', '阴': '正印'},
            '土': {'阳': '食神', '阴': '伤官'},
            '金': {'阳': '偏财', '阴': '正财'},
            '水': {'阳': '七杀', '阴': '正官'}
        },
        '土': {
            '土': {'阳': '比肩', '阴': '劫财'},
            '火': {'阳': '偏印', '阴': '正印'},
            '金': {'阳': '食神', '阴': '伤官'},
            '水': {'阳': '偏财', '阴': '正财'},
            '木': {'阳': '七杀', '阴': '正官'}
        },
        '金': {
            '金': {'阳': '比肩', '阴': '劫财'},
            '土': {'阳': '偏印', '阴': '正印'},
            '水': {'阳': '食神', '阴': '伤官'},
            '木': {'阳': '偏财', '阴': '正财'},
            '火': {'阳': '七杀', '阴': '正官'}
        }
    }
    """
    根据八字字符串计算每个天干的十神关系
    :param bazi_str: 八字字符串，例如 '戊寅甲寅壬辰癸卯'
    :return: 每个天干的十神关系（字典格式）
    """
    def get_shishen(day_gan, gan):
        """
        获取某个天干相对于日主的十神关系
        :param day_gan: 日主天干
        :param gan: 需要计算的天干
        :return: 十神名称
        """
        # 获取日主和目标天干的五行属性
        day_wuxing = GAN_WUXING[day_gan]
        target_wuxing = GAN_WUXING[gan]
        
        # 根据五行生克关系查找十神
        return SHISHEN_RELATION[day_wuxing][target_wuxing]
    
    
    # 提取日主天干（日柱的第一个字符）
    day_gan = bazi_list[2][0]
    
    # 计算每个天干的十神关系
    shishen_list = []
    for pillar in bazi_list:
        gan = pillar[0]
        day_wuxing = GAN_WUXING[day_gan]
        gan_wuxing = GAN_WUXING[gan]
        gan_yinyang = GAN_YINYANG[gan]
        shishen = SHISHEN_RELATION[day_wuxing][gan_wuxing][gan_yinyang]
        shishen_list.append(shishen)
    
    return shishen_list


    
    # 遍历八字中的每个天干
    for idx, pillar in enumerate(bazi):
        gan = pillar[0]  # 每柱的第一个字符是天干
        shishen = get_shishen(day_gan, gan)
        shishen_result[f'第{idx+1}柱'] = (gan, shishen)
    
    return shishen_result





async def calculate_bazi(date_str: str) -> dict:
    # 解析新历日期
    dt = datetime.strptime(date_str, "%Y%m%d %H")
    year, month, day, hour = dt.year, dt.month, dt.day, dt.hour

    # 将新历转换为农历
    solar = Solar.fromYmdHms(year, month, day, hour, 0, 0)
    lunar = solar.getLunar()
    eight_char = lunar.getEightChar()

    # 获取八字
    year_gan_zhi = eight_char.getYear()   # 年柱
    month_gan_zhi = eight_char.getMonth() # 月柱
    day_gan_zhi = eight_char.getDay()     # 日柱
    hour_gan_zhi = eight_char.getTime()   # 时柱

    baizi_list=[]
    baizi_list.append(year_gan_zhi)
    baizi_list.append(month_gan_zhi)
    baizi_list.append(day_gan_zhi)
    baizi_list.append(hour_gan_zhi)

    bazi_str=f"{year_gan_zhi}{month_gan_zhi}{day_gan_zhi}{hour_gan_zhi}"

    shishen = await calculate_shishen(baizi_list)

    # 返回结果
    return {
        "bazi": baizi_list,
        "shishen": shishen,
        "xin_time": f"{year}年{month}月{day}日{hour}时",
        "nong_time": f"{lunar.getYearInChinese()}年{lunar.getMonthInChinese()}月{lunar.getDayInChinese()}"
    }

# 测试
# if __name__ == "__main__":
#     result = calculate_shishen("戊寅甲寅壬辰癸卯")
#     print(result)

# 测试（异步函数需要用事件循环运行）
if __name__ == "__main__":
    import asyncio
    
    async def test():
        result = await calculate_bazi("19980214 06")
        print(result)
    
    asyncio.run(test())