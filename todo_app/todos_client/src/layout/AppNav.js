import styles from './AppNav.module.scss';
import {useAuth} from "../hooks/auth";
import {useEffect, useState} from "react";
import {Link, useLocation} from "react-router-dom";

const publicRoutes = [
    {
        text: 'Login',
        link: '/login',
    },
    {
        text: 'Register',
        link: '/register',
    },
];

const privateRoutes = [
    {
        text: 'Logout',
        link: '/logout',
    },
];

const AppNav = () => {
    const {isLoggedIn} = useAuth();
    const [currentRoute, setCurrentRoute] = useState(null);
    const [routes, setRoutes] = useState(publicRoutes);
    const location = useLocation();

    useEffect(() => {
        setRoutes(
            isLoggedIn
                ? privateRoutes
                : publicRoutes
        )
    }, [isLoggedIn]);

    useEffect(
        () => {
            let route = routes.find(r => r.link === location.pathname);
            if (!route) {
                route = routes[0]
            }
            setCurrentRoute(route);
        },
        [location, routes]
    );

    const renderLink = (route) => {
        const className = route.link === currentRoute?.link
            ? styles.disabled
            : '';
        return (
            <Link className={className} to={route.link}>{route.text}</Link>
        )
    }

    return (
        <nav>
            <ul className={styles.listNav}>
                {routes.map(r => (
                    <li key={r.link} className={styles.listNavItem}>
                        {renderLink(r)}
                    </li>
                ))}
            </ul>
        </nav>
    );
};

export default AppNav;
