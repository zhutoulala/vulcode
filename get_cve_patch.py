import os
import sys
import csv
import wget
import shutil

if __name__ == "__main__":
    
    download_folder = None
    if len(sys.argv) > 1:
        download_folder = sys.argv[1]
        if not os.path.exists(download_folder):
            os.mkdir(download_folder)

    print("Downloading latest CVE database...")
    CVE_list = wget.download("https://cve.mitre.org/data/downloads/allitems.csv")

    with open(CVE_list, mode='r', encoding="ISO-8859-1") as infile:
        reader = csv.reader(infile, quotechar='|')
        for row in reader:
            if len(row) < 4 or (not row[0].startswith("CVE")):
                continue
            CVE = row[0]
            links = row[3].split('|')
            patch_links = [x for x in links if x.find("https://github") != -1 and x.find("/commit/") != -1]
            if patch_links == []:
                continue
            for link in patch_links:
                link = link.strip(' "')
                if link.startswith("MISC:"):
                    link = link[5:]
                elif link.startswith("CONFIRM:"):
                    link = link[8:]
                try:
                    print("\nDownloading " + CVE + " patch: " + link)
                    out=CVE + ".patch"
                    if download_folder:
                        out = download_folder + os.sep + out
                    wget.download(link + ".patch", out = out)
                except:
                    pass