#!/usr/bin/env python3
"""Contrôle indicatif des URL externes. Internet nécessaire; aucun package à installer."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv, json, urllib.request, urllib.error, urllib.parse, ssl, re, sys

DIR=Path(__file__).resolve().parents[1]
IN=DIR/'data.js'
OUT=DIR/'RAPPORT-AUTO-LIENS.csv'

def check(url):
    if not url:return ('sans lien','', '')
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; SiteLinkAudit/1.0)','Accept':'text/html,application/xhtml+xml,*/*'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            status=resp.status
            final=resp.geturl()
            content_type=resp.headers.get('Content-Type','').lower()
            body=resp.read(14000).decode('utf-8','replace') if ('html' in content_type or not content_type) else ''
            low=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',body)).lower()
            if status>=500:return ('ERREUR_SERVEUR',str(status),final)
            if status==404:return ('404',str(status),final)
            if re.search(r'<title>\s*index of\s*/',body,re.I) or ('index of /' in low[:700] and len(low)<1000):return ('DOSSIER_SANS_SITE',str(status),final)
            if any(k in low[:600] for k in ['404 not found','page introuvable','error 404','page not found']):return ('PAGE_ERREUR_POSSIBLE',str(status),final)
            if len(body)<100 and 'html' in content_type:return ('A_CONTROLER','200',final)
            return ('OUVERT',str(status),final)
    except urllib.error.HTTPError as e:
        if e.code==404:return ('404','404',url)
        if e.code==410:return ('PAGE_SUPPRIMEE','410',url)
        return ('ACCES_REFUSE_OU_INDISPONIBLE',str(e.code),url) if e.code in (401,403,429,451) else ('ERREUR_HTTP',str(e.code),url)
    except Exception as e:return ('A_CONTROLER','',str(e)[:140])

def main():
    data=IN.read_text(encoding='utf-8')
    match=re.search(r'window\.GUIDE_PLACES\s*=\s*(\[.*?\]);',data,re.S)
    if not match:raise RuntimeError('Données GUIDE_PLACES non trouvées dans data.js')
    rows=json.loads(match.group(1))
    urls=sorted({u for r in rows for u in [r.get('website'),r.get('source')] if u})
    print('URLs uniques:',len(urls))
    outcomes={}
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures={ex.submit(check,u):u for u in urls}
        for future in as_completed(futures):
            u=futures[future]; outcomes[u]=future.result(); print(outcomes[u][0],u)
    with OUT.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f,delimiter=';');w.writerow(['Fiche','Type','URL','Diagnostic','HTTP','Adresse finale'])
        for r in rows:
            for field,kind in [('website','Site / fiche'),('source','Source')]:
                u=r.get(field)
                if u: w.writerow([r['name'],kind,u,*outcomes[u]])
    print('Rapport:',OUT)
    print('IMPORTANT : blocage anti-bot != lien cassé. Vérifier les diagnostics incertains dans un navigateur.')
    critical={'404','PAGE_SUPPRIMEE','DOSSIER_SANS_SITE','ERREUR_SERVEUR'}
    failures=[u for u,result in outcomes.items() if result[0] in critical]
    if failures:
        print('ERREURS A CORRIGER:',len(failures))
        for u in failures:print(' -',outcomes[u][0],u)
    return 1 if failures else 0
if __name__=='__main__':sys.exit(main())
