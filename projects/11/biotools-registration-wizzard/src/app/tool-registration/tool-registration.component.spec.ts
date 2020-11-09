import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ToolRegistrationComponent } from './tool-registration.component';

describe('ToolRegistrationComponent', () => {
  let component: ToolRegistrationComponent;
  let fixture: ComponentFixture<ToolRegistrationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ToolRegistrationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ToolRegistrationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
