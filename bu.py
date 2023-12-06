import os
import subprocess

# Function to detect SDK and NDK directories
def detect_android_dirs():
    # Try to detect the SDK directory from environment variables
    sdk_dir = os.environ.get("ANDROID_SDK_ROOT") or os.environ.get("ANDROID_HOME")

    # Try to detect the NDK directory from environment variables
    ndk_dir = os.environ.get("ANDROID_NDK_HOME")

    if sdk_dir is None or ndk_dir is None:
        print("Error: SDK or NDK directories not detected.")
        return None, None

    return sdk_dir, ndk_dir

# Run the p4a build command with detected directories
def build_with_detected_dirs():

 
    p4a_build_command = [
            "p4a",
            "apk",
            "--debug",
            "--requirements", "kivy==2.0.0,plyer,kivymd==1.1.1,json,pillow,urllib3",
            "--arch", "armeabi-v7a",
            "--api", "30",
            "--sdk_dir", "C:\\Users\\georg\\AppData\\Local\\Android\\Sdk",
            "--ndk_dir","C:\\Users\\georg\\Documents\\android-ndk-r26b-windows\\android-ndk-r26b"
        ]

    try:
        subprocess.check_call(p4a_build_command)
        print("Build completed successfully.")
    except subprocess.CalledProcessError as e:
            print(f"Build failed with error: {e}")
    
# Call the build function
build_with_detected_dirs()
