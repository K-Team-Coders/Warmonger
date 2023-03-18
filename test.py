from loguru import logger

current_domen =  'aeromotus'

def preprocessing_urls(urls):
    """
    Предобработка ссылок 
    """
    rubbish = 'jpg'

    cleaned = []
    for url in urls:
        # Нахождение ненужных юрлов по типу контакты, форумы и т.п.
        checker = False
        for item in rubbish:
            if item in url:
                checker = True        
        # Проверка на нахождение в том же домене (против бесконечных блужданий по интернету)
        domen_checker = False
        if current_domen in url:
            domen_checker = True

        # Финальный чек и проверка на PHP-производные сайты
        try:
            if not checker and domen_checker:
                cleaned.append(url)
            elif (not checker) and (url[0] == '/' and len(url) > 1):
                cleaned.append("https://" + current_domen + url)
            else:
                continue

        except IndexError:
            pass
    return cleaned

preprocessing_urls(['https://aeromotus.ru/wp-content/uploads/2019/08/mavic_2_ent_dual_section_10_details_1.jpg'])