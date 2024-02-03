import json
import re
#|â€¢

def cleanhtml(raw_html):
  CLEANER1 = re.compile('<.*?>')
  CLEANER2 = re.compile('â€¢')
  cleantext = re.sub(CLEANER1, '', raw_html)
  cleanertext = re.sub(CLEANER2, '>', cleantext)
  return cleanertext

def surround_with_asterisks(text, string_to_surround):
    pattern = re.escape(string_to_surround)
    replacement = r'**\g<0>**'
    result = re.sub(pattern, replacement, text)
    return result


def civilization(civ):
    with open('data/data.json') as f:
        data = json.load(f)

    locale_num = data['civ_helptexts'][civ]

    with open('data/locales/en/strings.json') as n:
        localdata = json.load(n)

    no_html = cleanhtml(localdata[locale_num])
    bold_text = surround_with_asterisks(no_html, "Unique Unit:")
    bold_text = surround_with_asterisks(bold_text, "Unique Techs:")
    bold_text = surround_with_asterisks(bold_text, "Team Bonus:")
    bold_text = "__**" + civ + "**__\n" + bold_text
    return bold_text


#print((civilization("Aztecs")))


