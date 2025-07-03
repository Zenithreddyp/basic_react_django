import "../styles/LoadingIndicator.css"

const LoadingIndicator = () => {
    return (
        <div className="loading-container">
            <div className="centered-wave-loader">
                <div className="centered-wave-bar"></div>
                <div className="centered-wave-bar"></div>
                <div className="centered-wave-bar"></div>
                <div className="centered-wave-bar"></div>
                <div className="centered-wave-bar"></div>
            </div>
        </div>
    );
}

export default LoadingIndicator