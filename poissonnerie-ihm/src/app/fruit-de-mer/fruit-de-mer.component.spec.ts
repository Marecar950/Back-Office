import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FruitDeMerComponent } from './fruit-de-mer.component';

describe('FruitDeMerComponent', () => {
  let component: FruitDeMerComponent;
  let fixture: ComponentFixture<FruitDeMerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FruitDeMerComponent]
    });
    fixture = TestBed.createComponent(FruitDeMerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
