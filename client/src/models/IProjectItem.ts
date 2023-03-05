export interface IRole {
    id: number;
    name: string;
    category: string;
}

export interface IUser {
    id: number;
    email: string;
    first_name: string;
    role: IRole;
}

export interface IOwner {
    id: number;
    email: string;
    first_name: string;
    role: IRole;
}

export interface IProjectItem {
    id: number;
    title: string;
    overview: string;
    owner: IOwner;
    users: IUser[];
    images: string;
    created: Date;
    search_for: IRole[];
}
