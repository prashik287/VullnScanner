import requests
from bs4 import BeautifulSoup
from colorama import Fore


# Get data from cve mitre


class cvemitre:
    def __init__(self, ):
        self.titles = []
        self.datas = []


    def getvuln(self,service):
        try:
            result = requests.get(f"https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={service}")
            # print(result.content)
            soup = BeautifulSoup(result.text, features="html.parser")
            table = soup.find("div", id="TableWithRules")
            # print(table)
            cekk = table.find_all("th")
            # print(cekk)
            epp = table.find_all("td")
            for i in cekk:
                title = i.text
                self.titles.append(title)
            # print(titles)
            for i, d in enumerate(epp):
                # Assuming d is an object with a 'text' attribute or method
                data = d.text  # Assuming d.text gives you the text content of d
                self.datas.append(data)
            print(Fore.RED + self.datas[0] + " : " + Fore.WHITE + self.datas[1])
        except IndexError as i:
            print("\n\nNo Vulnerability")
            for i in self.datas:
                print(i)
    
            return self.datas

        except Warning as w:
            print(w)
        except Exception as e:
            print(e)
#
# if __name__ == "__main__":
#     cv=cvemitre()
#     cv.getvuln("vsftpd 2.3.4")



