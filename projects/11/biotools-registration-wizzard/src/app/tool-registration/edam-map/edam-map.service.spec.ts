import { TestBed } from '@angular/core/testing';

import { EdamMapService } from './edam-map.service';

describe('EdamMapService', () => {
  let service: EdamMapService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EdamMapService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
