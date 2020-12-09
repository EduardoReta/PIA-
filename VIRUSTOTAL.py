"""
|------------------------------------|
|     Consulta de API VirusTotal     |
|------------------------------------|
"""
import argparse
import json
import os
import time
import requests
import logging

def scan(url_batch, api_key):
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    scan_id_list = []
    
    for u_r_l in url_batch:
        params = {'apikey': api_key, 'url': u_r_l}
        response = requests.post(url, data=params)
        scan_id_list.append(response.json()['scan_id'])        
    return scan_id_list

def report(scan_id_list, api_key):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    report_list = []

    for id_s in scan_id_list:
        params = {'apikey': api_key, 'resource': id_s}
        response = requests.get(url, params=params)
        report_list.append(response.json())
        
    return report_list


def virus_total(linkFiles, outputFile, responseFile, API_KEY):

    url_list = []
 
    output_file = open(outputFile, 'a')
    response_file = open(responseFile, 'a')


    with open(linkFiles) as f:
        for line in f:
            url_list.append(line.rstrip())

        response = []
        report_list = []
        for i in range(len(url_list)): 
            # If the quantity of request is equal to four, we have to wait a minute because 
            # of the limit of request.
            if i % 4 == 0:
                # API cooldown time is 60 seconds
                time.sleep(60)
                url_batch = []
            url_batch.append(url_list[i])

            # Tenemos que checar que obtuvimos 4 elementos, asi que podemos consultarlos
            # todos juntos, y si ese es el ultimo que no podemos consultar porque no podemos 
            # completa los 4 elementos
            if i % 4 == 3 or i == len(url_list) - 1:
                response += scan(url_batch, API_KEY)
                # Added line jump so we can distinguish between responses.
                # Guarda las las scan id's 
                response_file.write('\n'.join(str(t) for t in response))
                
                    
    print('scan complete')

    for i in range(len(response)):
        if i % 4 == 0:
            time.sleep(60)
            scan_list = []
        scan_list.append(response[i])
        if (i % 4 == 3 or i == len(response) - 1):
            report_bach = report(scan_list, API_KEY)
            report_list += report_bach
            for r in report_bach:
                json.dump(r, output_file)
                output_file.write("\n")
    output_file.close()
    response_file.close()