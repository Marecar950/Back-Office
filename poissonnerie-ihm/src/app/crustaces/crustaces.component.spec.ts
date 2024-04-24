import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrustacesComponent } from './crustaces.component';

describe('CrustacesComponent', () => {
  let component: CrustacesComponent;
  let fixture: ComponentFixture<CrustacesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CrustacesComponent]
    });
    fixture = TestBed.createComponent(CrustacesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
