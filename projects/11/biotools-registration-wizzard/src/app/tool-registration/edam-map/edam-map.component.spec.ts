import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EdamMapComponent } from './edam-map.component';

describe('EdamMapComponent', () => {
  let component: EdamMapComponent;
  let fixture: ComponentFixture<EdamMapComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EdamMapComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EdamMapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
