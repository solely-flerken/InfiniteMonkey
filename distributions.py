import numpy as np
from scipy.stats import gamma, expon, poisson
import matplotlib.pyplot as plt

# Parameters
MEAN_WAIT_TIME = 5 * 60 * 60 # seconds

# Gamma distribution parameters
GAMMA_SHAPE = 2
GAMMA_SCALE = MEAN_WAIT_TIME
GAMMA_OFFSET = 900 # seconds

# Uniform distribution parameters
MIN_DELAY = 3600  # 1 hour
MAX_DELAY = 43200 # 12 hours

def generate_random_waiting_time(distribution_type: str):
    if distribution_type == 'exponential':
        return np.random.exponential(MEAN_WAIT_TIME)
    elif distribution_type == 'gamma':
        return np.random.gamma(GAMMA_SHAPE, GAMMA_SCALE) + GAMMA_OFFSET
    elif distribution_type == 'uniform':
        return np.random.randint(MIN_DELAY, MAX_DELAY)
    else:
        raise ValueError("Unsupported distribution type. Choose 'uniform', 'exponential', or 'gamma'.")

def generate_samples(sample_size: int):
    """Generate random samples for Gamma and Exponential distributions."""
    gamma_samples = np.random.gamma(GAMMA_SHAPE, GAMMA_SCALE, sample_size)
    expon_samples = np.random.exponential(MEAN_WAIT_TIME, sample_size)
    uniform_samples = np.random.randint(MIN_DELAY, MAX_DELAY, sample_size)
    return gamma_samples, expon_samples, uniform_samples


def plot_gamma_distribution(gamma_samples, sample_size, offset=0):
    """Plot the Gamma distribution histogram and PDF with an offset."""
    # Apply the offset to the gamma samples
    gamma_samples_offset = gamma_samples + offset

    plt.figure(figsize=(10, 6))

    # Plot the histogram of the gamma samples with the offset applied
    plt.hist(gamma_samples_offset, bins=50, density=True, alpha=0.6, color='b', label='Gamma Distribution (Offset)')

    # Plot the Gamma PDF with the offset
    x = np.linspace(0, np.max(gamma_samples_offset), sample_size)
    pdf_gamma = gamma.pdf(x - offset, GAMMA_SHAPE, scale=GAMMA_SCALE)  # Shift the PDF by the offset
    plt.plot(x, pdf_gamma, 'r-', lw=2, label='Gamma PDF (Offset)')

    # Add a vertical line at the MEAN_WAIT_TIME with the offset
    plt.axvline(MEAN_WAIT_TIME + offset, color='green', linestyle='--',
                label=f'Mean = {(MEAN_WAIT_TIME + offset) / 3600:.1f} hours')

    # Set the plot labels and title
    plt.title("Gamma Distribution with Offset")
    plt.xlabel("Waiting Time (seconds)")
    plt.ylabel("Density")
    plt.legend(loc="best")
    plt.grid(True)

    # Show the plot
    plt.show()


def plot_exponential_distribution(expon_samples, sample_size):
    """Plot the Exponential distribution histogram and PDF."""
    plt.figure(figsize=(10, 6))
    plt.hist(expon_samples, bins=50, density=True, alpha=0.6, color='orange', label='Exponential Distribution')

    # Plot the Exponential PDF
    x = np.linspace(0, np.max(expon_samples), sample_size)
    pdf_expon = expon.pdf(x, scale=MEAN_WAIT_TIME)
    plt.plot(x, pdf_expon, 'g--', lw=2, label='Exponential PDF')

    # Add a vertical line at the MEAN_WAIT_TIME
    plt.axvline(MEAN_WAIT_TIME, color='green', linestyle='--', label=f'Mean = {MEAN_WAIT_TIME / 3600:.1f} hours')

    plt.title("Exponential Distribution")
    plt.xlabel("Waiting Time (seconds)")
    plt.ylabel("Density")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()

def plot_uniform_distribution(uniform_samples, sample_size, lower_bound, upper_bound):
    """Plot the Uniform distribution histogram."""
    plt.figure(figsize=(10, 6))
    plt.hist(uniform_samples, bins=50, density=True, alpha=0.6, color='b', label='Uniform Distribution')

    # Plot the Uniform PDF (although it's just a constant)
    x = np.linspace(lower_bound, upper_bound, sample_size)
    pdf_uniform = np.ones_like(x) / (upper_bound - lower_bound)
    plt.plot(x, pdf_uniform, 'r-', lw=2, label=f'Uniform PDF ({lower_bound}, {upper_bound})')

    # Add a vertical line at the MEAN_WAIT_TIME
    plt.axvline(MEAN_WAIT_TIME, color='green', linestyle='--', label=f'Mean = {MEAN_WAIT_TIME / 3600:.1f} hours')

    plt.title(f"Uniform Distribution: U({lower_bound}, {upper_bound})")
    plt.xlabel("Waiting Time (seconds)")
    plt.ylabel("Density")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()

def test_distributions(sample_size: int = 1000):
    """Test and visualize the Gamma, Exponential, and Poisson distributions."""
    # Generate random samples
    gamma_samples, expon_samples, uniform_samples = generate_samples(sample_size)

    # Plot Gamma, Exponential, and Poisson distributions
    plot_gamma_distribution(gamma_samples, sample_size, GAMMA_OFFSET)
    plot_exponential_distribution(expon_samples, sample_size)
    # plot_uniform_distribution(uniform_samples, sample_size, MIN_DELAY, MAX_DELAY)

if __name__ == '__main__':
    test_distributions()
