import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SpinnerService {

  constructor() { }

  private loading = false;

  show(): void {
    this.loading = true;
  }

  hide(): void {
    this.loading = false;
  }

  isLoading(): boolean {
    return this.loading;
  }
}
