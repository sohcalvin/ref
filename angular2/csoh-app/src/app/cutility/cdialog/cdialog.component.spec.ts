import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CdialogComponent } from './cdialog.component';

describe('CdialogComponent', () => {
  let component: CdialogComponent;
  let fixture: ComponentFixture<CdialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CdialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CdialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
