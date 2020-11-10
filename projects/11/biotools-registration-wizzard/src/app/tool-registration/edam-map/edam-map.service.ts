import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class EdamMapService {

    constructor(private httpClient: HttpClient) {}

    getEDAM(searchOptions: any): Observable<any> {

        return this.httpClient.post<any>('/edammap/api',
            searchOptions,
            {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
    }

}
