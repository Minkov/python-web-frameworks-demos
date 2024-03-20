import {useCallback, useState} from "react";
import {useAuth} from "../hooks/auth";
import {Button, TextField} from "@mui/material";
import {Navigate} from 'react-router-dom';
import {withLayout} from "./base/LayoutPage";
import styles from "./LoginPage.module.scss";
import loginPage from "./LoginPage";

const RegisterPage = () => {
    const [isSuccessful, setSuccessful] = useState(false);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const {
        register,
        login,
    } = useAuth();

    const handleClick = useCallback(
        async () => {
            await register(username, password);
            await login(username, password);
            setSuccessful(true);
        },
        [register, username, password, login]
    );

    if (isSuccessful) {
        return (
            <Navigate to='/'/>
        );
    }

    return (
        <div className={styles.container}>
            <h2>Register</h2>
            <form onSubmit={() => handleClick()}>
                <div className={styles.row}>
                    <TextField
                        label="Enter username"
                        variant="standard"
                        className={styles.formControl}
                        onChange={(ev) => setUsername(ev.target.value)}/>
                </div>
                <div className={styles.row}>
                    <TextField
                        label="Enter password"
                        variant="standard"
                        type="password"
                        className={styles.formControl}
                        onChange={(ev) => setPassword(ev.target.value)}/>
                </div>

                <div className={styles.row}>
                    <Button
                        variant="contained"
                        onClick={() => handleClick()}>
                        Register
                    </Button>
                </div>
            </form>
        </div>
    );
};

export default withLayout(RegisterPage);