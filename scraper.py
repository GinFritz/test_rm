# Python test code

import scraperwiki
import BeautifulSoup
import urllib2
import string

#CREATE TABLE 'albo_milano' ('Codice Fiscale' text, 'Progressivo' integer, 'Cognome' text, 'Nome' text, 'Email' text, 'Tel' text, 'Fax' text, 'CAP' text, 'Indirizzo' text)


lastrec = 25000
i = 1

while i < lastrec:
    try:
        html = scraperwiki.scrape('http://www.ordineavvocati.roma.it/AlboElenchi/AlboAvvocati/SchedaIscritto.asp?ID=' + str(i))
        soup = BeautifulSoup.BeautifulSoup(html)
        id_avv=i
        print id_avv
        i=i+1
        j=1
        for dato_avv in soup.findAll('td'):
            x = str(dato_avv)
            j=j+1
            if j==13:
                cognome = str(dato_avv.string)
                #print cognome
            elif j==15:
                nome = str(dato_avv.string)
                #print nome
            elif j==21:
                codfisc = str(dato_avv.string)
                #print codfisc
            elif j==29:
                indiriz = str(dato_avv.string)
                #print indiriz
            elif j==31:
                citta = str(dato_avv.string)
                #print citta
            elif j==33:
                cap = str(dato_avv.string)
                #print cap
            elif j==35:
                tel = str(dato_avv.string)
                #print tel
            elif j==37:
                fax = str(dato_avv.string)
                #print fax
        k=1
        for dato_avv in soup.findAll('a'):
            x = str(dato_avv)
            k=k+1
            if k==4:
                email = str(dato_avv.string)
                print email

        scraperwiki.sqlite.save(unique_keys=["Codice fiscale"], data = {"Codice fiscale":codfisc, "Tel":tel, "Fax":fax, "Email":email, "Nome":nome, "Cognome":cognome, "Citta":citta, "CAP":cap, "Indirizzo":indiriz, "Progressivo":id_avv})

    except:
        i=i+1
        continue
