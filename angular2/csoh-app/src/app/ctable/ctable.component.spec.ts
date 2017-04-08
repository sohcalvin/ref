import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CtableComponent } from './ctable.component';

describe('CtableComponent', () => {
  let component: CtableComponent;
  let fixture: ComponentFixture<CtableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CtableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CtableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
