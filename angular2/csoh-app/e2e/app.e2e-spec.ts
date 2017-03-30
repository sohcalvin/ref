import { CsohAppPage } from './app.po';

describe('csoh-app App', () => {
  let page: CsohAppPage;

  beforeEach(() => {
    page = new CsohAppPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
