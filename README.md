# Ethereum Paper Wallet Generator

A simple Python application to generate Ethereum paper wallets with private keys, public addresses, and QR codes. This tool is designed to help users securely generate and store their Ethereum credentials offline.

## Security Notice

**Important:** For maximum security, ensure that your computer is disconnected from the internet (Wi-Fi and Ethernet) before generating your Ethereum paper wallet. This reduces the risk of your private keys being exposed to online threats.

## Features

- **Secure Key Generation:** Generates Ethereum private keys and public addresses using the `eth_keys` library.
- **Seed Phrase Creation:** Produces a 24-word seed phrase for wallet recovery, leveraging the `mnemonic` library.
- **QR Code Display:** Generates and displays QR codes for both the private key and public address for easy scanning.
- **High-Resolution Image Saving:** Allows users to save wallet details as a high-resolution image for offline storage.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Criul1/EthereumPaperWallet.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd EthereumPaperWallet
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:
```bash
python ethpaperwallet.py
```

Follow the on-screen instructions to generate your Ethereum paper wallet. The application will display the private key, public address, and seed phrase, along with QR codes for the private key and public address.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the project's coding standards and includes appropriate tests..

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out via [GitHub Issues](https://github.com/Criul1/EthereumPaperWallet/issues).....
