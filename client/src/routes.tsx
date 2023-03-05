import { AppRoutes } from './helpers/consts';
import Auth from './views/Auth';
import Home from './views/Home';
import Profile from './views/Profile';
import Project from './views/Project';

export const publicRoutes = [
	{
		path: AppRoutes.HOME,
		Component: Auth,
	},

];


export const privateRoutes = [
	{
		path: AppRoutes.HOME,
		Component: Home,
	},

	{
		path: AppRoutes.PROFILE,
		Component: Profile
	},

	{
		path: AppRoutes.PROJECT + '/:id',
		Component: Project,
	},
];

