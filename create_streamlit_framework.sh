mkdir .streamlit
touch .streamlit/config.toml
echo '[client]' >> .streamlit/config.toml
echo 'showErrorDetails = "none"' >> .streamlit/config.toml
echo '' >> .streamlit/config.toml
echo '[theme]' >> .streamlit/config.toml
echo 'base= "light"' >> .streamlit/config.toml
echo 'primaryColor = "#F63366"' >> .streamlit/config.toml
echo 'backgroundColor = "white"' >> .streamlit/config.toml
echo '' >> .streamlit/config.toml
echo '[server]' >> .streamlit/config.toml
echo 'runOnSave = true' >> .streamlit/config.toml
echo 'maxUploadSize = 5' >> .streamlit/config.toml
touch app.sh
echo 'pip3 install -r requirements.txt' >> app.sh
echo 'streamlit run main.py --server.port 8501' >> app.sh
echo 'streamlit' >> requirements.txt
rm create_streamlit_framework.sh