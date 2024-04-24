import { TestBed } from '@angular/core/testing';

import { PoissonsService } from './poissons.service';

describe('PoissonsService', () => {
  let service: PoissonsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PoissonsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
