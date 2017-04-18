export class User {
  constructor(
    
    public email: string,
    public firstName: string,
    public lastName: string,
    public password: string,
    public roles : string[],
    public id?: number
  ) {  }
}