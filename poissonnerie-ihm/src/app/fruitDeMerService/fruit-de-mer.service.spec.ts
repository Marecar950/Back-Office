import { TestBed } from '@angular/core/testing';

import { FruitDeMerService } from './fruit-de-mer.service';

describe('FruitDeMerService', () => {
  let service: FruitDeMerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FruitDeMerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
